import { ApolloServer, gql } from 'apollo-server'
import resolvers from './resolvers.js'

const typeDefs = gql`
  ${require('./schema.graphql')}
`

const server = new ApolloServer({
  typeDefs,
  resolvers
})

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`)
})