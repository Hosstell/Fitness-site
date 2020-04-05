<template>
  <v-app dark>
    <notifications group="notify"/>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      temporary
    >
      <v-list>
        <v-list-item>
          Вы вошли как {{ $$user.lastName }} {{ $$user.firstName[0] }}.
        </v-list-item>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <app-bar @changeMenuState="drawer = !drawer"/>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import AppBar from "./AppBar";

export default {
  components: {AppBar},
  middleware: 'auth-middleware',
  data () {
    return {
      clipped: true,
      drawer: false,
      fixed: false,
      items: [{
          icon: 'mdi-account',
          title: 'Личный кабинет',
          to: '/lk'
        }, {
          icon: 'mdi-account-multiple',
          title: 'Тренера',
          to: '/trainers'
        }, {
          icon: 'mdi-account-group',
          title: 'Клиенты',
          to: '/clients'
        }, {
          icon: 'mdi-dumbbell',
          title: 'Тренировки',
          to: '/workouts'
        }, {
          icon: 'mdi-calendar-multiple-check',
          title: 'События',
          to: '/events'
        }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>
