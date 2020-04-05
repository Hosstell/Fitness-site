<template>
  <div>
    <v-card>
      <v-card-title>
        <v-toolbar
          flat
          class="py-0">
          <span class="headline">
            Список тренировок
          </span>
          <v-spacer/>
          <v-btn class="mr-3" @click="$refs.createSeasonTicket.openDialog()" color="primary">
            Добавить абонемент
          </v-btn>

          <v-btn @click="$refs.createWorkoutDialog.openDialog()" color="primary">
            Добавить новую тренировку
          </v-btn>
        </v-toolbar>
      </v-card-title>

      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="workouts.items"
          :server-items-length="workouts.count"
        >
          <template slot="item" slot-scope="props">
            <tr @click="editWorkout(props.item.id)">

              <td>
                <v-btn @click.stop="props.expand(!props.isExpanded)" icon>
                  <v-icon>
                    {{ props.isExpanded ? 'mdi-chevron-up' : 'mdi-chevron-down'}}
                  </v-icon>
                </v-btn>
              </td>

              <td>
                {{ props.item.name }}
              </td>

              <td>
                <div v-for="trainer in props.item.trainers">
                  <v-icon  v-if="trainer.sex === 'M'" color="blue">
                    mdi-human-male
                  </v-icon>
                  <v-icon v-else color="pink">
                    mdi-human-female
                  </v-icon>

                  {{ trainer.firstName }}
                  {{ trainer.lastName }}
                </div>
              </td>

              <td>
                <div v-for="datetime in props.item.datetime">
                  {{ datetime.weekday }} {{ datetime.time.slice(0, 5) }}
                </div>
              </td>
            </tr>
          </template>

          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length" class="px-0">
              <workout-clients-table
                :workoutId="item.id"
              />
            </td>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <create-workout-dialog ref="createWorkoutDialog" @created="allWorkoutRequest"/>
    <create-season-ticket-dialog ref="createSeasonTicket" />
    <edit-workout-dialog ref="editWorkoutDialog" @updated="allWorkoutRequest" @deleted="allWorkoutRequest"/>
  </div>
</template>

<script>
  import utilsMixin from "../utils/utils";
  import CreateWorkoutDialog from "../components/workouts/CreateWorkoutDialog";
  import EditWorkoutDialog from "../components/workouts/EditWorkoutDialog";
  import WorkoutClientsTable from "../components/workouts/WorkoutClientsTable";
  import requests from "../components/user/requests";
  import CreateSeasonTicketDialog from "../components/workouts/CreateSeasonTicketDialog";

  export default {
    name: "workouts",
    components: {CreateSeasonTicketDialog, WorkoutClientsTable, EditWorkoutDialog, CreateWorkoutDialog},
    mixins: [utilsMixin],
    data() {
      return {
        headers: [{
          text: '',
        }, {
          text: 'Название',
          align: 'left',
          value: 'name',
          sortable: false,
        }, {
          text: 'Тренера',
          align: 'left',
          value: 'trainers',
          sortable: false,
        }, {
          text: 'Время',
          align: 'left',
          value: 'time',
          sortable: false,
        }],
        workouts: {
          items: [],
          count: 0
        }
      }
    },
    methods: {
      editWorkout(workoutId) {
        this.$refs.editWorkoutDialog.editWorkout(workoutId)
      },
      allWorkoutRequest() {
        requests.getAllWorkouts(this.$apollo)
        .then(({data}) => {
          this.workouts = {
            items: data.getAllWorkouts,
            count: data.getAllWorkouts.length
          }
        })
      }
    },
    mounted() {
      this.allWorkoutRequest()
    }
  }
</script>

<style scoped>

</style>