<template>
  <v-menu
    ref="menu"
    :close-on-content-click="false"
    v-model="menu"
    :disabled="disabled || readonly"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
        v-on="on"
        :label="label"
        v-model="formattedValue"
        :prepend-icon="prependIcon"
        :rules="rules"
        readonly
        :disabled="disabled"
        :hide-details="hideDetails"
        :required="required"
      />
    </template>
    <v-time-picker
      v-model="innerValue"
      autosave
      format="24hr"
      :width="$vuetify.breakpoint.name === 'xs' ? 230 : 290"
      @change="$refs.menu.save(innerValue)"
    />
  </v-menu>
</template>

<script>
export default {
  name: 'time-picker',
  props: {
    disabled: Boolean,
    label: String,
    prependIcon: String,
    readonly: Boolean,
    rules: Array,
    value: String,
    hideDetails: Boolean,
    required: Boolean
  },
  data() {
    return {
      innerValue: this.value,
      menu: false
    }
  },
  watch: {
    value(newValue) {
      this.innerValue = newValue
    },
    innerValue(newValue) {
      this.$emit('input', newValue)
    }
  },
  computed: {
    formattedValue() {
      if (this.innerValue) {
        return this.innerValue.substr(0, 5)
      } else {
        return ''
      }
    }
  }
}
</script>

<style scoped></style>
