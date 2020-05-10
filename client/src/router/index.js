import Vue from 'vue'
import Router from 'vue-router'
import EmployeeForm from '@/components/EmployeeForm'
import AllUsers from '@/components/AllUsers.vue'
import UpdateForm from '@/components/UpdateForm'
Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/users',
            name: 'AllUsers',
            component: AllUsers
        },
        {
            path: '/users',
            name: 'AllUsers',
            component: AllUsers
        },

        {
            path: '/adduser',
            name: 'employee-form',
            component: EmployeeForm
        },
        {
            path: '/updateuser/:id',
            name: 'update-form',
            component: UpdateForm,
            props: true
        }


    ]
})