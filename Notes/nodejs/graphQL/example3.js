const { ApolloServer, gql } = require("apollo-server");
const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const typeDefs = gql`
  type Todo {
    id: Int!
    title: String!
    is_completed: Boolean!
  }

  type Query {
    todos: [Todo]
  }

  type Mutation {
    createTodo(title: String!): Todo
  }
`;

const resolvers = {
  Query: {
    todos: () => prisma.todos.findMany(),
  },
  Mutation: {
    createTodo: (_, { title }) => prisma.todos.create({ data: { title } }),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});

// In this example, the server defines a Todo type with id, title, and is_completed fields. The Query type includes a todos field for retrieving all todo items. The Mutation type includes a createTodo field for creating a new todo item.
// The createTodo resolver creates a new todo item using the Prisma client. The todos resolver retrieves all todo items from the Prisma client.