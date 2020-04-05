<template>
  <div>

    <client-select
      label="Клиент*"
      v-model="form.clientId"
      :rules="[rules.notNullValue]"
      required
    />

    <workout-select
      label="Тренировка*"
      v-model="form.workoutId"
      :rules="[rules.notNullValue]"
      required
    />

    <v-row>
      <v-col cols="6">
        <date-picker
          label="Дата начала*"
          v-model="form.startDate"
          :rules="[rules.notNullValue]"
          required
        />
      </v-col>

      <v-col cols="6">
        <date-picker
          label="Дата конца*"
          v-model="form.endDate"
          :allowed-dates="allowedDate"
          :rules="[rules.notNullValue]"
          required
        />
      </v-col>
    </v-row>

  </div>
</template>

<script>
  import WeekDaySelect from "../WeekDaySelect";
  import TrainersSelect from "./TrainersSelect";
  import TimePicker from "../common/TimePicker";
  import ClientSelect from "../clients/ClientSelect";
  import WorkoutSelect from "./WorkoutSelect";
  import DatePicker from "../common/DatePicker";

  export default {
    name: "SeasonTicketForm",
    components: {DatePicker, WorkoutSelect, ClientSelect, TimePicker, TrainersSelect, WeekDaySelect},
    props: {
      form: Object
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
        allowedDate: date => !this.form.startDate || date > this.form.startDate
      }
    },
    methods: {
      addNewDateTime() {
        this.form.datetime.push({
          weekday: null,
          time: ''
        })
      },
      removeDatetime(index) {
        this.form.datetime.splice(index, 1)
      }
    }
  }
</script>

<style scoped>

</style>