import gql from 'graphql-tag'

const getCurrentUser = gql`
  query {
    getCurrentUser {
      id
      firstName
      lastName
      sex
      birthDate
    }
  }
`

export { getCurrentUser }
