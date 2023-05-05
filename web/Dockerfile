FROM node:lts

ENV APP_HOME=/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ENV APP_USER=appuser
ENV APP_GROUP=app
RUN addgroup --system $APP_GROUP && adduser --system $APP_USER && adduser $APP_USER $APP_GROUP

COPY package.json .
COPY pnpm-lock.yaml .
COPY .npmrc .

RUN npm install -g pnpm
RUN pnpm pkg set scripts.prepare="nuxt prepare"
RUN pnpm install --prod

COPY . .

RUN pnpm build

RUN chown -R $APP_USER:$APP_GROUP $APP_HOME
USER $APP_USER

CMD node .output/server/index.mjs
