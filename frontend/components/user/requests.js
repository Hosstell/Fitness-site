import gql from 'graphql-tag'

export default {
  getAllUsers(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllUsers {
            id
            firstName
            lastName
            birthDate
            sex
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  },
  getAllClients(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllClients {
            id
            firstName
            lastName
            birthDate
            sex
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  },
  getAllWorkouts(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllWorkouts {
            id
            name
            trainers {
              id
              firstName
              lastName
              sex
            }
            datetime: workouttimeSet {
              id
              time
              weekday: rusWeekday 
            }
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  },
  getCurrentWorkout(apollo, workoutId) {
    return apollo.query({
      query: gql`
        query($workoutId: String!) {
          getCurrentWorkout(workoutId: $workoutId) {
            id
            name
            trainers {
              id
              firstName
              lastName
              sex
            }
            datetime: workouttimeSet {
              id
              time
              weekday: rusWeekday 
            }
          }
        }
      `,
      variables: { workoutId },
      fetchPolicy: 'no-cache'
    })
  },
  createWorkout(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation ($input: CreateWorkoutInput!) {
          createWorkout(input: $input) {
            status
          }
        }
      `,
      variables: { input },
      fetchPolicy: 'no-cache'
    })
  },
  editWorkout(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: EditWorkoutInput!) {
          editWorkout(input: $input) {
            status
          }
        }
      `,
      variables: { input },
      fetchPolicy: 'no-cache'
    })
  },
  deleteWorkout(apollo, workoutId) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: DeleteWorkoutInput!) {
          deleteWorkout(input: $input) {
            status
          }
        }
      `,
      variables: {
        input: { id: workoutId }
      },
      fetchPolicy: 'no-cache'
    })
  },
  createSeasonTicket(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: CreateSeasonTicketInput!) {
          createSeasonTicket(input: $input) {
            status
          }
        }
      `,
      variables: { input },
      fetchPolicy: 'no-cache'
    })
  },
  saveSeasonTicket(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: SaveSeasonTicketInput!) {
          saveSeasonTicket(input: $input) {
            status
          }
        }
      `,
      variables: { input },
      fetchPolicy: 'no-cache'
    })
  },
  getSeasonTickets(apollo, workoutId) {
    return apollo.query({
      query: gql`
        query($workoutId: String!) {
          getSeasonTickets(workoutId: $workoutId) {
            id
            client {
              id
              firstName
              lastName
              birthDate
              sex
            }
            workout {
              id
              name
            }
            startDate
            endDate
          }
        }
      `,
      variables: { workoutId: workoutId },
      fetchPolicy: 'no-cache'
    })
  },
  getCurrentSeasonTicket(apollo, seasonTicketId) {
    return apollo.query({
      query: gql`
        query($seasonTicketId: String!) {
          getCurrentSeasonTicket(seasonTicketId: $seasonTicketId) {
            id
            client {
              id
              firstName
              lastName
              birthDate
              sex
            }
            workout {
              id
              name
            }
            startDate
            endDate
          }
        }
      `,
      variables: { seasonTicketId: seasonTicketId },
      fetchPolicy: 'no-cache'
    })
  },
  deleteSeasonTicket(apollo, seasonTicketId) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: DeleteSeasonTicketInput!) {
          deleteSeasonTicket(input: $input) {
            status
          }
        }
      `,
      variables: {
        input: { id: seasonTicketId }
      },
      fetchPolicy: 'no-cache'
    })
  },
  createEvent(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation($input: CreateEventInput!) {
          createEvent(input: $input) {
            status
          }
        }
      `,
      variables: {
        input
      },
      fetchPolicy: 'no-cache'
    })
  },
  getAllWorkoutEvent(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllEvents {
            id
            workout {
              id
              name
            }
            clients {
              id
              firstName
              lastName
              sex
            }
            trainers {
              id
              firstName
              lastName
              sex
            }
            creator {
              id
              firstName
              lastName
              sex
            }
            createDate
            date
            time
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  },
  editUser(apollo, input) {
    return apollo.mutate({
      mutation: gql`
        mutation ($input: EditUserInput!) {
          editUser(input: $input) {
            status
          }
        }
      `,
      variables: { input },
      fetchPolicy: 'no-cache'
    })
  },
  getWorkoutOfUser(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllWorkoutOfUser {
            id
            name
            datetime: workouttimeSet {
              id
              time
              weekday: rusWeekday 
            }
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  },
  getAllWorkoutEventsOfUser(apollo) {
    return apollo.query({
      query: gql`
        query {
          getAllWorkoutEventsOfUser {
            id
            workout {
              id
              name
            }
            date
            time
          }
        }
      `,
      fetchPolicy: 'no-cache'
    })
  }
}