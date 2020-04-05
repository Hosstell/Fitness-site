<template>
  <div>
    <v-card>
      <v-card-title>
        <v-toolbar
          flat
          class="py-0">
          <span class="headline">
            Список событий
          </span>
          <v-spacer/>
          <v-btn color="primary" @click="$refs.createEventDialog.openDialog()">
            Создать событие
          </v-btn>
        </v-toolbar>
      </v-card-title>

      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="workoutEvents.items"
          :server-items-length="workoutEvents.count"
          :sort-by.sync="pagination.sortBy"
          :sort-desc.sync="pagination.desc"
        >
          <template slot="item" slot-scope="props">
            <tr>

              <td>
                <v-btn @click.stop="props.expand(!props.isExpanded)" icon>
                  <v-icon>
                    {{ props.isExpanded ? 'mdi-chevron-up' : 'mdi-chevron-down'}}
                  </v-icon>
                </v-btn>
              </td>

              <td>
                <sex-icon :sex="props.item.creator.sex" />
                {{ props.item.creator.firstName }}
                {{ props.item.creator.lastName }}

                <div>
                  {{ formatDateTime(props.item.createDate) }}
                </div>
              </td>

              <td>
                {{ props.item.workout.name }}
              </td>

              <td>
                {{ formatDate(props.item.date) }}
                {{ props.item.time.slice(0, 5) }}
              </td>

              <td>
                <div v-for="trainer in props.item.trainers">
                  <sex-icon :sex="trainer.sex"/>
                  {{ trainer.firstName }}
                  {{ trainer.lastName }}
                </div>
              </td>
            </tr>
          </template>

          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
              <div>
                Список клиентов:
              </div>
              <div class="pb-2">
                <span v-for="client in item.clients" class="pr-2">
                  <v-chip class="chip--select-multi chip--project">
                    <span class="mr-2" >
                      <sex-icon :sex="client.sex"/>
                    </span>

                    {{ client.firstName }}
                    {{ client.lastName }}
                  </v-chip>
                </span>
              </div>
            </td>
          </template>

        </v-data-table>
      </v-card-text>
    </v-card>

    <create-events ref="createEventDialog"/>
  </div>
</template>

<script>
  import utilsMixin from "../utils/utils";
  import CreateEvents from "../components/events/CreateEvents";
  import requests from "../components/user/requests";
  import SexIcon from "../components/common/SexIcon";

  export default {
    name: "events",
    components: {SexIcon, CreateEvents},
    mixins: [utilsMixin],
    data() {
      return {
        headers: [{
          text: '',
        }, {
          text: 'Создатель',
          align: 'left',
          value: 'sex',
        }, {
          text: 'Тренировка',
          align: 'left',
          value: 'workout',
        }, {
          text: 'Дата и время проведения',
          align: 'left',
          value: 'datetime',
        }, {
          text: 'Тренера',
          align: 'left',
          value: 'sex',
        }],
        pagination: {
          sortBy: '',
          desc: []
        },
        workoutEvents: {
          items: [],
          count: 1
        }
      }
    },
    methods: {
      allWorkoutEventsRequest() {
        requests.getAllWorkoutEvent(this.$apollo)
        .then(({data}) => {
          this.workoutEvents = {
            items: data.getAllEvents,
            count: data.getAllEvents.length
          }
          console.log(data)
        })
      }
    },
    computed: {
      // items() {
      //   let items = _.sortBy(this.clients.items, this.pagination.sortBy)
      //   if (this.pagination.desc.length && this.pagination.desc[0]) {
      //     items = items.reverse()
      //   }
      //   return items
      // }
    },
    mounted() {
      this.allWorkoutEventsRequest()
    }
  }
</script>

<style scoped>

</style>