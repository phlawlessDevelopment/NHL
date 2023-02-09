import { derived, writable } from 'svelte/store';

export const posts = writable([])

export const latestPosts = derived(posts, (posts) => posts.sort((a, b) => b.date - a.date).slice(0, 5))