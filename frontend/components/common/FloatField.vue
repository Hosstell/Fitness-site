<template>
  <v-text-field
    :label="label"
    :required="required"
    :disabled="disabled"
    v-model="convert"
    :rules="isNumber"
    :suffix="suffix"
    :hide-details="hideDetails"
    :readonly="readonly"
    ref="textField"
    :prefix="prefix"
    :placeholder="placeholder"
    :reverse="reverse"
    :persistent-hint="persistentHint"
    :hint="hint"
  />
</template>

<script>
export default {
  name: 'FloatField',
  props: {
    value: Number,
    label: String,
    required: Boolean,
    disabled: Boolean,
    readonly: Boolean,
    hideDetails: Boolean,
    suffix: String,
    prefix: {
      type: String,
      default: ''
    },
    rules: {
      type: Array,
      default: () => []
    },
    notZero: Boolean,
    placeholder: String,
    reverse: Boolean,
    persistentHint: Boolean,
    hint: String
  },
  data() {
    return {
      variable: this.value,
      isNumber: [
        text => {
          let result = /^-?\d+((,|\.).\d*)?$/.test(text)
          if (!result) {
            return 'Неверный формат'
          }
          if (this.notZero && parseFloat(text) === 0) {
            return 'Сумма не должна быть 0'
          }

          return true
        },
        ...this.rules
      ]
    }
  },
  computed: {
    convert: {
      get: function() {
        if (this.variable || this.variable === 0) {
          return String(this.variable).replace('.', ',')
        } else {
          return ''
        }
      },
      set: function(text) {
        this.variable = text
        const val = parseFloat(this.variable.replace(',', '.'))
        if (!isNaN(val)) {
          this.$emit('input', val)
        } else if (text === '') {
          this.$emit('input', null)
        }
        this.$emit('change')
      }
    }
  },
  methods: {
    focus() {
      this.$refs.textField.focus()
    },
    validate() {
      this.$refs.textField.validate()
    }
  },
  watch: {
    value: function(val) {
      this.variable = val
    }
  }
}
</script>
