import { createRouter, createWebHistory } from 'vue-router';

import TestComponents from './TestComponents.vue';

const routes = [
	{
		path: '/',
		component: TestComponents
	}
]

const router = createRouter({
	history: createWebHistory('/'),
	routes
});

export default router;