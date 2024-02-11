<template>
    <div>
        <div>
            Email Scheduler Status  {{ enabled? ".":"" }}
        </div>
        <div>
            <v-switch hide-details inset v-model="enabled" :label="schedulerStatus ? 'Active' : 'Inactive'"
                @change="handleChange" color="primary"></v-switch>

        </div>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    props: {
        value: Boolean
    },
    data() {
        return {
            enabled: this.value
        }
    },

    methods: {
        async handleChange() {
            try {
                this.$emit('change-scheduler', this.enabled)
            } catch (error) {
                console.error('Error :', error);
            }
        }
    }
})
</script>
  