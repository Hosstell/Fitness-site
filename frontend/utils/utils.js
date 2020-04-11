import moment from 'moment'
import Lockr from 'lockr'


moment.locale('ru-ru')

const utilsMixin = {
  methods: {
    formatDate(textDate) {
      if (textDate) {
        return moment(textDate).format('L')
      } else {
        return ''
      }
    },
    formatDateRus(date) {
      const reg = /^(\d{2})\.(\d{2})\.(\d{4}|\d{2})$/
      let str = ''
      if (date) {
        str = date.split(String.fromCharCode(8206)).join('')
        if (reg.test(str)) {
          const isoDate = moment(date, 'DD-MM-YYYY')
            .utc(true)
            .toISOString()
          if (isoDate) {
            return isoDate.substring(0, 10)
          }
        }
      }
      return null
    },
    formatMonth(date) {
      if (date) {
        return moment(date).format('DD MMMM YYYY')
      } else {
        return ''
      }
    },
    formatDateTime(textDateTime) {
      if (textDateTime) {
        return moment(textDateTime).format('L LT')
      } else {
        return ''
      }
    },
    storeValue(name, val) {
      const _name = this.$options.name + '$' + name
      if (process.client) {
        Lockr.set(_name, val)
      }
    },
    getValue(name, emptyVal) {
      const _name = this.$options.name + '$' + name
      if (process.client) {
        return Lockr.get(_name, emptyVal)
      }
      return emptyVal
    },
    getFullAge(birthDate) {
      return (new Date() - new Date(birthDate)) / 1000 / 60 / 60 / 24 / 365
    }
  }
}

export default utilsMixin
