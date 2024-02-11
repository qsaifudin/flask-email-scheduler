<template>
    <v-dialog  width="500px">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props" text="Add Email" color="primary" dark> </v-btn>
        </template>
        <template v-slot:default="{ isActive }">
            <v-card>
            <v-card-title>Add New Email</v-card-title>
            <v-card-text>
                <v-form @submit.prevent="saveEmail">
                    <v-text-field v-model="formData.event_id" label="Event ID"></v-text-field>
                    <v-text-field v-model="formData.email_subject" label="Email Subject"></v-text-field>
                    <v-textarea rows="3" v-model="formData.email_content" label="Email Content"></v-textarea>
                    <v-text-field v-model="formData.timestamp" label="Timestamp"></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="saveEmail">Save</v-btn>
                <v-btn color="primary" @click="dialog = false">Cancel</v-btn>
            </v-card-actions>
            </v-card>
        </template>
    </v-dialog>
</template>
  
<script>
export default {
    data() {
        return {
            formData: {
                event_id: '',
                email_subject: '',
                email_content: '',
                timestamp: ''
            }
        }
    },
    methods: {
        saveEmail() {
            this.$emit('add-email', this.formData);
            this.dialog = false;
        }
    }
}
</script>
  