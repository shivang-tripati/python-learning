// To set up a GraphQL server, you will need to define your schema and resolvers. 
// The schema defines the types of data that your API can provide, and the resolvers define how those types of data are obtained
// Here's an example of a simple GraphQL schema:
/*
type Query {
  pets: [Pet]
  pet(id: Int!): Pet
}

// In this schema, we have defined a Query type that has two fields: pets and pet.
 The pets field returns a list of Pet objects, while the pet field returns a single Pet object with a specific id.


type Pet {
  id: Int!
  name: String!
  type: String!
  breed: String!
}

// The Pet type has four fields: id, name, type, and breed. 
Each field has a type associated with it, such as Int for integers and String for strings.
*/

/* Next, we need to define the resolvers for our schema. The resolvers define how the data for each field is obtained. Here's an example of resolvers for our Query type: */

const resolvers = {
    Query: {
      pets: () => {
        return [
          { id: 1, name: 'Fido', type: 'Dog', breed: 'Labrador' },
          { id: 2, name: 'Bella', type: 'Dog', breed: 'Poodle' },
          { id: 3, name: 'Whiskers', type: 'Cat', breed: 'Tabby' },
        ]
      },
      pet: (_, { id }) => {
        return { id, name: `Pet ${id}`, type: 'Unknown', breed: 'Unknown' }
      },
    },
  }
/* In this example, we have defined two resolvers: one for the pets field and one for the pet field.
The pets resolver simply returns an array of Pet objects. The pet resolver takes an id argument and returns a Pet object with that id */
// To implement a GraphQL server, you can use a library like Apollo Server. Here's an example of how to set up a GraphQL server using Apollo Server:

import { ApolloServer, gql } from 'apollo-server'

const typeDefs = gql`
  type Query {
    pets: [Pet]
    pet(id: Int!): Pet
  }

  type Pet {
    id: Int!
    name: String!
  }`