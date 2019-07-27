var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
'/static/images/icon.png',
'/static/images/splash.png',
//'/templates/base/base.html',
//'/templates/base/leftsidebar.html',
//'/templates/base/pageloader.html',
//'/templates/base/js.html',
//'/templates/base/topbar.html',
//'/templates/index/index.html',
//'/templates/index/changepassword.html',
//'/templates/index/signup.html',
//'/templates/index/forgotpassword.html'
];

// Cache on install
self.addEventListener("install", event => {
this.skipWaiting();
event.waitUntil(
caches.open(staticCacheName)
.then(cache => {
return cache.addAll(filesToCache);
})
)
});

// Clear cache on activate
self.addEventListener('activate', event => {
event.waitUntil(
caches.keys().then(cacheNames => {
return Promise.all(
cacheNames
.filter(cacheName => (cacheName.startsWith("django-pwa-")))
.filter(cacheName => (cacheName !== staticCacheName))
.map(cacheName => caches.delete(cacheName))
);
})
);
});

// Serve from Cache
self.addEventListener("fetch", event => {
event.respondWith(
caches.match(event.request)
.then(response => {
return response || fetch(event.request);
})
.catch(() => {
return caches.match('offline');
})
)
});