<template>
  <div>
    <v-card>
      <v-card-title>
        <v-toolbar
          flat
          class="py-0">
          <span class="headline">
            Список тренеров
          </span>
        </v-toolbar>
      </v-card-title>

      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="items"
          :server-items-length="trainers.count"
          :sort-by.sync="pagination.sortBy"
          :sort-desc.sync="pagination.desc"
          mobile-breakpoint="0"
        >
          <template slot="item" slot-scope="props">
            <tr>

              <td>
                <v-icon  v-if="props.item.sex === 'M'" color="blue">
                  mdi-human-male
                </v-icon>
                <v-icon v-else color="pink">
                  mdi-human-female
                </v-icon>
              </td>

              <td>
                {{ props.item.firstName }}
              </td>

              <td>
                {{ props.item.lastName }}
              </td>

              <td>
                {{ getFullAge(props.item.birthDate).toFixed(0) }} ({{ formatDate(props.item.birthDate) }})
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

  </div>
</template>

<script>
  import utilsMixin from "../utils/utils";
  import gql from 'graphql-tag';
  import requests from "../components/user/requests.js"
  import _ from "lodash";

  export default {
    name: "trainers",
    mixins: [utilsMixin],
    data() {
      return {
        headers: [{
          text: 'Пол',
          align: 'left',
          value: 'sex'
        }, {
          text: 'Имя',
          align: 'left',
          value: 'firstName'
        }, {
          text: 'Фамилия',
          align: 'left',
          value: 'lastName'
        }, {
          text: 'Возраст',
          align: 'left',
          value: 'birthDate'
        }],
        pagination: {
          sortBy: null,
          desc: []
        },
        trainers: {
          items: [{
            firstName: 'Андрей',
            lastName: 'Серов',
            birthDate: '1996-10-21',
            sex: 'M'
          }],
          count: 1
        }
      }
    },
    computed: {
      items() {
        let items = _.sortBy(this.trainers.items, this.pagination.sortBy)
        if (this.pagination.desc.length && this.pagination.desc[0]) {
          items = items.reverse()
        }
        return items
      }
    },
    mounted() {
      requests.getAllUsers(this.$apollo).then(({data}) => {
        this.trainers = {
          items: data.getAllUsers,
          count: data.getAllUsers.length
        }
      })
    }
  }
</script>

<style scoped>

</style>