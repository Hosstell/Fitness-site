<template>
  <v-card>
    <v-card-title>
      Личные данные
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="6" class="py-0">
          <v-text-field
            label="Имя"
            v-model="user.firstName"
          />
        </v-col>

        <v-col cols="12" sm="6" class="py-0">
          <v-text-field
            label="Фамилия"
            v-model="user.lastName"
          />
        </v-col>

        <v-col cols="12" sm="6" class="py-0">
          <sex-select
            v-model="user.sex"
          />
        </v-col>

        <v-col cols="12" sm="6" class="py-0">
          <date-picker
            label="День рождение"
            v-model="user.birthDate"
          />
        </v-col>

      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn color="primary" @click="saveUser" :loading="loading">
        Сохранить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  import SexSelect from "../common/SexSelect";
  import DatePicker from "../common/DatePicker";
  import requests from "../user/requests";


  export default {
    name: "PrivateData",
    components: {DatePicker, SexSelect},
    data() {
      return {
        loading: false,
        user: {
          firstName: '',
          lastName: '',
          sex: '',
          birthDate: ''
        }
      }
    },
    methods: {
      saveUser() {
        this.loading = true
        requests.editUser(
          this.$apollo,
          {
            userId: this.$$user.id,
            firstName: this.user.firstName,
            lastName: this.user.lastName,
            birthDate: this.user.birthDate,
            sex: this.user.sex
          }
        ).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно изменили личныые данные',
            text: ''
          })
          this.loading = false

        }).catch(e => {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Произошла ошибка при изменение личных данных',
            text: ''
          })
          this.loading = false
        })
      }
    },
    mounted() {
      let checkUser = () => {
        return this.$$user.id
      }

      let loadUser = () => {
        if (checkUser()) {
          this.user = {
            firstName: this.$$user.firstName,
            lastName: this.$$user.lastName,
            sex: this.$$user.sex,
            birthDate: this.$$user.birthDate
          }
        } else {
          setTimeout(loadUser)
        }
      }

      loadUser()
    }
  }
</script>

<style scoped>

</style>