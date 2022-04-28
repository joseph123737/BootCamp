import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/home/HomePage.vue'
import Quizz from '@/pages/quizz/QuizzPage.vue'
import Quizzes from '@/pages/quizzes/QuizzesPage.vue'
import Result from '@/pages/result/ResultPage.vue'
import User from '@/pages/user/UserPage.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/quizzes/quizz/:id',
    name: 'quizz',
    component: Quizz,
  },
  {
    path: '/quizzes',
    name: 'quizzes',
    component: Quizzes,
  },
  {
    path : '/quizz/result',
    name:'result',
    component : Result
  },
  {
    path:'/user/:id',
    name:'user',
    component:User
  },
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
