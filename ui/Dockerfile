# ---------- Build Stage ----------
FROM node:18 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build --configuration=production

# ---------- Run Stage ----------
FROM nginx:alpine

# Angular build copy (⚠ project name "ui" hona chahiye)
COPY --from=build /app/dist/ui /usr/share/nginx/html

# Nginx routing config
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
