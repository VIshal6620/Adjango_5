# ---------- Build stage ----------
FROM node:18 AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build --configuration=production


# ---------- Nginx stage ----------
FROM nginx:alpine

# remove default config
RUN rm /etc/nginx/conf.d/default.conf

# COPY nginx.conf FIRST
COPY nginx.conf /etc/nginx/conf.d/default.conf

# then copy build output
COPY --from=build /app/dist/ui /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
