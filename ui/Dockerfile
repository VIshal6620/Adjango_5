# Stage 1 – Build Angular
FROM node:20 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build -- --project ui --configuration production

# Stage 2 – Nginx
FROM nginx:alpine

# ✅ COPY CORRECT DIST PATH
COPY --from=build /app/dist/ui/ /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
