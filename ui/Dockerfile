# -------- Build Stage --------
FROM node:18 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build --configuration=production

# -------- Run Stage --------
FROM nginx:alpine

# IMPORTANT: Angular project name yahan match karo
COPY --from=build /app/dist/ui /usr/share/nginx/html

# Angular routing fix
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
