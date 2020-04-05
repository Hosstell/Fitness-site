<template>
  <div>
    <v-text-field
      label="Имя*"
      v-model="client.firstName"
      :rules="[rules.notNullValue]"
      required
    />

    <v-text-field
      label="Фамилия*"
      v-model="client.lastName"
      :rules="[rules.notNullValue]"
      required
    />

    <date-picker
      label="День рождение*"
      v-model="client.birthDate"
      :rules="[rules.notNullValue]"
      required
    />

    <v-select
      label="Пол*"
      v-model="client.sex"
      :items="genders"
      item-text="name"
      item-value="value"
      :rules="[rules.notNullValue]"
      required
    />
  </div>
</template>

<script>
  import DatePicker from "../common/DatePicker";
  export default {
    name: "ClientForm",
    components: {DatePicker},
    props: {
      client: Object
    },
    data() {
      return {
        rules: {
          notNullValue: value => !!value || "Поле не должно быть пустым",
          more7letters: value => value.length > 7 || "Пароль должен быть длинее 7 символов",
          emailRule: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Неверный формат email'
          }
        },
        genders: [{
          name: 'Мужчина',
          value: "M"
        }, {
          name: "Женщина",
          value: "F"
        }]
      }
    }
  }
</script>

<style scoped>

</style>