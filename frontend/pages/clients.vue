<template>
  <div>
    <v-card>
      <v-card-title>
        <v-toolbar
          flat
          class="py-0">
          <span class="headline">
            Список клиентов
          </span>
          <v-spacer/>

          <v-btn
            v-if="this.$vuetify.breakpoint.xs"
            @click="$refs.createClientDialog.openDialog()"
            color="primary"
            icon
            outlined
          >
            <v-icon> mdi-plus </v-icon>
          </v-btn>

          <v-btn v-else @click="$refs.createClientDialog.openDialog()" color="primary">
            Добавить нового клиента
          </v-btn>


        </v-toolbar>
      </v-card-title>

      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="items"
          :server-items-length="clients.count"
          :sort-by.sync="pagination.sortBy"
          :sort-desc.sync="pagination.desc"
          mobile-breakpoint="0"
        >
          <template slot="item" slot-scope="props">
            <tr @click="editClient(props.item.id)">

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
                {{ Math.trunc(getFullAge(props.item.birthDate)) }} лет ({{ formatDate(props.item.birthDate) }})
              </td>
            </tr>

          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <create-client-dialog ref="createClientDialog" @created="updateList"/>
    <edit-client-dialog ref="editClientDialog" @updated="updateList" @deleted="updateList"/>
  </div>
</template>

<script>
  import utilsMixin from "../utils/utils";
  import CreateClientDialog from "../components/clients/CreateClientDialog";
  import EditClientDialog from "../components/clients/EditClientDialog";
  import gql from "graphql-tag";
  import _ from "lodash";

  export default {
    name: "clients",
    components: {EditClientDialog, CreateClientDialog},
    mixins: [utilsMixin],
    data() {
      return {
        headers: [{
          text: 'Пол',
          align: 'left',
          value: 'sex',
          width: '10px'
        }, {
          text: 'Имя',
          align: 'left',
          value: 'firstName'
        }, {
          text: 'Фамилия',
          align: 'left',
          value: 'lastName',
        }, {
          text: 'Возраст',
          align: 'left',
          value: 'birthDate',
        }],
        pagination: {
          sortBy: '',
          desc: []
        },
        clients: {}
      }
    },
    apollo: {
      query: {
        query: gql`
        query {
          getAllClients {
            id
            firstName
            lastName
            birthDate
            sex
          }
        }`,
        update(data) {
          this.clients = {
            items: data.getAllClients,
            count: data.getAllClients.length
          }
        }
      }
    },
    methods: {
      editClient(clientId) {
        this.$refs.editClientDialog.editClient(clientId)
      },
      updateList() {
        this.$apollo.queries.query.refetch()
      }
    },
    computed: {
      items() {
        let items = _.sortBy(this.clients.items, this.pagination.sortBy)
        if (this.pagination.desc.length && this.pagination.desc[0]) {
          items = items.reverse()
        }
        return items
      }
    }
  }
</script>

<style scoped>

</style>