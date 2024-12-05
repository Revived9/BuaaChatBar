<template>
  <div class="success-dialog">
    <div class="success-content">
      <div class="checkmark-circle">
        <div class="checkmark draw"></div>
      </div>
      <p>{{ message }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

const props = defineProps({
  message: {
    type: String,
    default: '操作成功'
  }
});

const emit = defineEmits(['close']);

onMounted(() => {
  setTimeout(() => {
    emit('close');
  }, 1000);
});
</script>

<style scoped>
.success-dialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.success-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.checkmark-circle {
  width: 50px;
  height: 50px;
  position: relative;
  display: inline-block;
  vertical-align: top;
  margin-bottom: 10px;
}

.checkmark-circle .background {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: #4CAF50;
  position: absolute;
}

.checkmark-circle .checkmark {
  border-radius: 5px;
}

.checkmark-circle .checkmark.draw:after {
  content: "";
  width: 25px;
  height: 12.5px;
  position: absolute;
  border: 2px solid #4CAF50;
  border-top: none;
  border-right: none;
  background: transparent;
  left: 12.5px;
  top: 18.75px;
  transform: rotate(-45deg);
  animation: checkmark 0.3s ease-in-out forwards;
}

@keyframes checkmark {
  0% {
    height: 0;
    width: 0;
    opacity: 1;
  }
  20% {
    height: 0;
    width: 12.5px;
    opacity: 1;
  }
  40% {
    height: 12.5px;
    width: 25px;
    opacity: 1;
  }
  100% {
    height: 12.5px;
    width: 25px;
    opacity: 1;
  }
}
</style>
