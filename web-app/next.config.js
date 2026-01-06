/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Enable static export for GitLab Pages deployment
  output: 'export',
  // Disable image optimization for static export
  images: {
    unoptimized: true,
  },
  // Set base path if deploying to a subdomain (uncomment and modify if needed)
  // basePath: '/tech-mastery-notebooks',
  webpack: (config) => {
    config.resolve.fallback = { fs: false, path: false };
    return config;
  },
}

module.exports = nextConfig
