# frontend/Dockerfile
FROM nginx:stable-alpine
# Simple static HTML that talks to backend API
COPY ./dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
