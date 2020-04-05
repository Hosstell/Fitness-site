<template>
  <v-select
    label="Пол*"
    v-model="sex"
    :items="genders"
    item-text="name"
    item-value="value"
    :rules="[rules.notNullValue]"
    required
  />
</template>

<script>
  export default {
    name: "sex-select",
    props: {
      value: String,
    },
    data() {
      return {
        sex: this.value,
        genders: [{
          name: 'Мужчина',
          value: "M"
        }, {
          name: "Женщина",
          value: "F"
        }],
        rules: {
          notNullValue: value => !!value || "Поле не должно быть пустым",
        },
      }
    },
    watch: {
      value: function (newVal) {
        this.sex = newVal
      },
      sex: function (newVal) {
        this.$emit('input', newVal)
      }
    }
  }
</script>

<style scoped>

</style>