<template>
    <v-card>
        <v-card-title class="my-3 align-center text-lg-center">Emails Scheduler</v-card-title>
        <v-data-table :headers="headers" :items="emails" item-key="event_id" class="elevation-1">
            <template v-slot:item.timestamp="{ item }">
                {{ new Date(item.timestamp).toLocaleString() }}
            </template>
            <template v-slot:item.status="{ item }">
                <v-badge :color="getStatusColor(item.status)" :content="item.status">
                    
                </v-badge>
            </template>

        </v-data-table>
    </v-card>
</template>
  
<script>
export default {
    props: {
        emails: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            headers: [
                { title: 'Event ID', key: 'event_id' },
                { title: 'Email Subject', key: 'email_subject' },
                { title: 'Email Content', key: 'email_content' },
                { title: 'Timestamp', key: 'timestamp' },
                { title: 'Status Sending', key: 'status' },
            ]
        }
    },
    methods: {
        getStatusColor(status) {
            return status == 'pending' ? 'red' : 'green' // Adjust colors as needed
        }
    }
}
</script>
  
<style scoped>
.elevation-1 {
    box-shadow: none;
}
</style>
  