import React from 'react'
import ReactDOM from 'react-dom'
import { ApolloClient, InMemoryCache, ApolloProvider, gql } from '@apollo/client'
import { PetList } from './components/PetList'

const client = new ApolloClient({
  uri: 'http://localhost:4000',
  cache: new InMemoryCache()
})

const GET_PETS = gql`
  query GetPets {
    pets {
      id
      name
      type
      breed
      age
    }
  }
`

ReactDOM.render(
  <ApolloProvider client={client}>
    <PetList query={GET_PETS} />
  </ApolloProvider>,
  document.getElementById('root')
)