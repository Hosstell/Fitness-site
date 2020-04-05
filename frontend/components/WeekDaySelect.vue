<template>
  <v-select
    v-model="selectWeekday"
    :label="label"
    :items="weekdays"
    :hide-details="hideDetails"
    :rules="[requiredFun]"
    :required="required"
  />
</template>

<script>
  export default {
    name: "WeekDaySelect",
    props: {
      value: String,
      label: String,
      hideDetails: Boolean,
      required: Boolean
    },
    data() {
      return {
        weekdays: [
          'Понедельник',
          'Вторник',
          'Среда',
          'Четверг',
          'Пятница',
          'Суббота',
          'Воскресенье'
        ],
        selectWeekday: this.value,
        requiredFun: text => !this.required || !!text || "Поле не может быть пустым"
      }
    },
    watch: {
      selectWeekday: function (newVal) {
        this.$emit('input', newVal)
      },
      value: function (newVal) {
        this.selectWeekday = newVal
      }
    }
  }
</script>

<style scoped>

</style>