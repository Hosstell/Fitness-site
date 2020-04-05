<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="seasonTickets"
      hide-default-footer
      dense
    >
      <template slot="item" slot-scope="props">
        <tr @click="editSeasonTicket(props.item.id)">

          <td>
            <v-icon  v-if="props.item.client.sex === 'M'" color="blue">
              mdi-human-male
            </v-icon>
            <v-icon v-else color="pink">
              mdi-human-female
            </v-icon>
          </td>

          <td>
            {{ props.item.client.firstName }} {{ props.item.client.lastName }}
          </td>

          <td>
            {{ getFullAge(props.item.client.birthDate).toFixed(0) }} ({{ formatDate(props.item.client.birthDate) }})
          </td>

          <td>
            {{ formatDate(props.item.startDate) }} -
            {{ formatDate(props.item.endDate)}}

            ( Осталось дней:
            {{ (((new Date(props.item.endDate)) - (new Date())) / 3600 / 24 / 1000).toFixed(0) }}
            )
          </td>

        </tr>
      </template>
    </v-data-table>

    <edit-season-ticket
      ref="editSeasonTicket"
      @updated="allSeasonsOfWorkoutRequest"
      @deleted="allSeasonsOfWorkoutRequest"/>
  </div>
</template>

<script>
  import utilsMixin from "../../utils/utils";
  import requests from "../user/requests.js";
  import EditSeasonTicket from "./EditSeasonTicket";

  export default {
    name: "WorkoutClientsTable",
    components: {EditSeasonTicket},
    props: {
      workoutId: String
    },
    mixins: [utilsMixin],
    data() {
      return {
        headers: [{
          text: 'Пол',
          align: 'left',
          value: 'sex',
          sortable: false,
        }, {
          text: 'ФИО',
          align: 'left',
          value: 'first_name',
          sortable: false,
        }, {
          text: 'Возраст',
          align: 'left',
          value: 'birth_date',
          sortable: false,
        }, {
          text: 'Даты абонемента',
          align: 'left',
          value: 'birth_date',
          sortable: false,
        }],
        seasonTickets: []
      }
    },
    methods: {
      allSeasonsOfWorkoutRequest() {
        requests.getSeasonTickets(this.$apollo, this.workoutId)
        .then(({data}) => {

          console.log(data)
          this.seasonTickets = data.getSeasonTickets
        })
      },
      editSeasonTicket(seasonTicketId) {
        this.$refs.editSeasonTicket.editSeasonTicket(seasonTicketId)
      }
    },
    mounted() {
      this.allSeasonsOfWorkoutRequest()
    }
  }
</script>

<style scoped>

</style>