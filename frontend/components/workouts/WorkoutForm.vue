<template>
  <div>
    <v-text-field
      label="Название*"
      v-model="form.name"
      :rules="[rules.notNullValue]"
      required
    />

    <trainers-select
      v-model="form.trainers"
      label="Тренера*"
      multiple
      chips
      required
      :rules="[rules.notNullValue]"
      clearable
    />

    <div v-for="(datetime, index) in form.datetime">
      <v-row>
        <v-col cols="8" class="py-0">
          <week-day-select
            label="День недели*"
            v-model="datetime.weekday"
            hide-details
            required
          />
        </v-col>
        <v-col cols="3" class="py-0">
          <time-picker
            label="Время*"
            v-model="datetime.time"
            :rules="[rules.notNullValue]"
            hide-details
            required
          />
        </v-col>
        <v-col cols="1" class="py-0 pt-3 pr-6">
          <v-btn
            v-if="form.datetime.length !== 1"
            @click="removeDatetime(index)"
            icon
          >
            <v-icon color="red">
              mdi-delete
            </v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </div>

    <v-row>
      <v-spacer/>
      <v-btn icon @click="addNewDateTime" class="mr-3">
        <v-icon color="green">
          mdi-plus
        </v-icon>
      </v-btn>
    </v-row>
  </div>
</template>

<script>
  import WeekDaySelect from "../WeekDaySelect";
  import TrainersSelect from "./TrainersSelect";
  import TimePicker from "../common/TimePicker";

  export default {
    name: "WorkoutForm",
    components: {TimePicker, TrainersSelect, WeekDaySelect},
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
        }
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