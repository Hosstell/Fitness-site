<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6" xl="4">
        <v-form v-model="formValid">
          <v-card>
            <v-card-title class="pa-0">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Регистрация в системе "Fit Active"</v-toolbar-title>
                <v-spacer/>
              </v-toolbar>

            </v-card-title>
            <v-card-text>
              <v-text-field
                label="Имя*"
                v-model="form.firstName"
                :rules="[rules.notNullValue]"
                required
              />

              <v-text-field
                label="Фамилия*"
                v-model="form.lastName"
                :rules="[rules.notNullValue]"
                required
              />

              <date-picker
                label="День рождение*"
                v-model="form.birthDate"
                :rules="[rules.notNullValue]"
                required
              />

              <v-select
                label="Пол*"
                v-model="form.sex"
                :items="genders"
                item-text="name"
                item-value="value"
                :rules="[rules.notNullValue]"
                required
              />

              <v-divider class="pb-2"/>

              <v-text-field
                label="Email*"
                v-model="form.email"
                :rules="[rules.notNullValue, rules.emailRule]"
                required
              />

              <v-text-field
                label="Пароль*"
                v-model="form.password"
                :append-icon="hidePassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="hidePassword = !hidePassword"
                :type="hidePassword ? 'text' : 'password'"
                counter
                :rules="[rules.notNullValue, rules.more7letters]"
                required
              />
            </v-card-text>
            <v-card-actions>
              <v-btn text @click="$router.push({path: '/login'})">
                Вход
              </v-btn>
              <v-spacer/>
              <v-btn color="primary" :disabled="!formValid" @click="registration">
                Зарегистрироваться
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import DatePicker from "../components/common/DatePicker";
  import gql from 'graphql-tag';

  export default {
    name: "registration",
    components: {DatePicker},
    layout: 'login',
    data() {
      return {
        form: {
          firstName: '',
          lastName: '',
          birthDate: '',
          sex: '',
          email: '',
          password: '',
        },
        genders: [{
          name: 'Мужчина',
          value: "M"
        }, {
          name: "Женщина",
          value: "F"
        }],
        formValid: false,
        rules: {
          notNullValue: value => !!value || "Поле не должно быть пустым",
          more7letters: value => value.length > 7 || "Пароль должен быть длинее 7 символов",
          emailRule: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Неверный формат email'
          }
        },

        hidePassword: false
      }
    },
    methods: {
      registration() {
        this.$apollo.mutate({
          mutation: gql`
          mutation ($input: RegistrationInput!) {
            registration(input: $input) {
              result
            }
          }`,
          variables: {
            input: {
              firstName: this.form.firstName,
              lastName: this.form.lastName,
              birthDate: this.form.birthDate,
              sex: this.form.sex,
              email: this.form.email,
              password: this.form.password,
            }
          }
        }).then(data => {
          this.$notify({
            group: 'notify',
            title: 'Вы успешно зарегистрировались',
            text: ''
          })

          this.$router.push({ path: '/login' })
        })
      }
    }
  }
</script>

<style scoped>

</style>
