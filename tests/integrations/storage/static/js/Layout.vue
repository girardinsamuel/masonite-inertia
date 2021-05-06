<template>
  <div>
    <slot />
    <div class="p-4 fixed bottom-0 inset-x-0 mt-10 bg-gray-100 rounded-md space-y-2">
      <p>Inertia Page data: <span class="rounded-md px-2 text-sm font-medium py-1 bg-gray-300 text-red-700">{{ $page.props }}</span></p>
      <p>Inertia Component: <span class="rounded-md px-2 text-sm font-medium py-1 bg-gray-300 text-red-700">{{ $page.component }}</span></p>
      <p>Inertia URL: <span class="rounded-md px-2 text-sm font-medium py-1 bg-gray-300 text-red-700">{{ $page.url }}</span></p>
      <p>Inertia Assets version: <span class="rounded-md px-2 text-sm font-medium py-1 bg-gray-300 text-red-700">{{ $page.version }}</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Layout"
}
</script>
