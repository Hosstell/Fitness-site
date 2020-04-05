<template>
  <v-autocomplete
    v-model="selectClients"
    :items="clients"
    :label="label"
    :required="required"
    :readonly="readonly"
    :clearable="clearable"
    ref="select"
    :multiple="multiple"
    :disabled="disabled"
    :hide-details="hideDetails"
    item-text="lastName"
    item-value="id"
    :chips="chips"
    :rules="rules"
  >
    <template slot="selection" slot-scope="data">
      <v-chip
        class="chip--select-multi chip--project"
      >
        <span class="mr-2" >
          <v-icon  v-if="data.item.sex === 'M'" color="blue">
            mdi-human-male
          </v-icon>
          <v-icon v-else color="pink">
            mdi-human-female
          </v-icon>
        </span>

        {{ data.item.firstName }}
        {{ data.item.lastName }}
      </v-chip>
    </template>

    <template slot="item" slot-scope="data">
      <div>
        <v-icon  v-if="data.item.sex === 'M'" color="blue">
          mdi-human-male
        </v-icon>
        <v-icon v-else color="pink">
          mdi-human-female
        </v-icon>

        {{ data.item.firstName }}
        {{ data.item.lastName }}
      </div>
    </template>

  </v-autocomplete>
</template>

<script>
  import requests from "../user/requests.js"

  export default {
    name: "ClientSelect",
    props: {
      value: null,
      label: String,
      multiple: Boolean,
      required: Boolean,
      readonly: Boolean,
      hideDetails: Boolean,
      disabled: Boolean,
      clearable: Boolean,
      returnObject: Boolean,
      rules: {
        type: Array,
        default: () => []
      },
      chips: Boolean,
    },
    data() {
      return {
        selectClients: this.value,
        clients: [{
          firstName: 'Андрей',
          lastName: 'Серов',
          sex: 'M'
        }, {
          firstName: 'Виктория',
          lastName: 'Самарская',
          birthDate: '1997-01-12',
          sex: 'F'
        }]
      }
    },
    methods: {
      allClientsRequest() {
        requests.getAllClients(this.$apollo).then(({data}) => {
          this.clients = data.getAllClients
        })
      }
    },
    watch: {
      selectClients: function (newVal) {
        this.$emit('input', newVal)
      },
      value: function (newVal) {
        this.selectClients = newVal
      }
    },
    mounted() {
      this.allClientsRequest()
    }
  }
</script>

<style scoped>

</style>