<!-- pages/index.vue -->
<template>
  <v-app>
    <v-app-bar fixed app>
      <v-btn class="ml-12">
        <NuxtLink class="" to="https://qsaifudin.site/" target="_blank" style="color: white; text-decoration: none;">
          <v-toolbar-title>
            <h3 style="font-size: 30px;">👉<span class="animate-text">Saifudin</span> </h3>
          </v-toolbar-title>
        </NuxtLink>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-row class="justify-center align-center">
          <v-spacer></v-spacer>
          <SchedulerSwitch class="mr-3" v-model="schedulerEnabled" />
          <AddEmailDialog @add-email="addEmail" />
        </v-row>
        <EmailTable :emails="emails" />
      </v-container>
    </v-main>
  </v-app>
</template>


<script>
import EmailTable from '~/components/EmailTable.vue'
import SchedulerSwitch from '~/components/SchedulerSwitch.vue'
import AddEmailDialog from '~/components/AddEmailDialog.vue'

export default {
  components: {
    EmailTable,
    AddEmailDialog,
    SchedulerSwitch
  },
  data() {
    return {
      emails: [],
      schedulerStatus: false,
      BASE_URL: useRuntimeConfig().public.BASE_URL
    }
  },
  async mounted() {
    await this.fetchEmails()
    await this.fetchSchedulerStatus()
  },
  methods: {
    async fetchEmails() {
      try {
        const emailsResponse = await $fetch(this.BASE_URL + '/emails/all')
        const archiveEmailsResponse = await $fetch(this.BASE_URL + '/archived_emails/all')

        const emails = emailsResponse.data.map(email => ({ ...email, status: 'pending' }))
        const archiveEmails = archiveEmailsResponse.data.map(email => ({ ...email, status: 'success' }))



        this.emails = [...emails, ...archiveEmails]
      } catch (error) {
        console.error('Error fetching emails:', error)
      }
    },
    async fetchSchedulerStatus() {
      try {
        const response = await $fetch(this.BASE_URL +'/scheduler/status')
        this.schedulerStatus = response.status
      } catch (error) {
        console.error('Error fetching scheduler status:', error)
      }
    },
    async addEmail(emailData) {
      try {
        await $fetch(this.BASE_URL +'/save_emails', {
          method: 'POST',
          body: JSON.stringify(emailData)
        })
        await this.fetchEmails()
      } catch (error) {
        console.error('Error adding email:', error)
      }
    },
    async toggleScheduler(status) {
      try {
        await $fetch(this.BASE_URL +'/scheduler/toggle', {
          method: 'POST',
          body: JSON.stringify({ status })
        })
      } catch (error) {
        console.error('Error toggling scheduler:', error)
      }
    }
  }
}

</script>
<style scoped>
.graph {
  width: 800px;
  height: 600px;
  border: 1px solid #000;
}

.animate-text {
  font-family: 'Open Sans';
  font-weight: 800;
  font-size: 30px;
  background: linear-gradient(to right,
      currentColor 0,
      #a2ebd58f 10%,
      currentColor 20%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: borderAnimate 10s infinite alternate;
}

@keyframes borderAnimate {

  0%,
  100% {
    background-position: -100px;
  }

  50% {
    background-position: 510px;
  }
}
</style>
