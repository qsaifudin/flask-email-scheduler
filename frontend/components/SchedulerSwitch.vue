<template>
    <v-switch v-model="enabled" @change="handleChange" label="Toggle Email Scheduler" color="primary"></v-switch>
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
        handleChange() {
            this.$emit('change', this.enabled)
        }
    }
})
</script>
  