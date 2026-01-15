# Stage 1 – Build Angular
FROM node:20 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build -- --configuration production

# Stage 2 – Nginx
FROM nginx:alpine

# 🔥 SPA routing fix
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/dist/*/ /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
