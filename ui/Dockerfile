# Step 1 — Build Angular
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build --prod

# Step 2 — Serve using Nginx
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /app/dist/ui /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
