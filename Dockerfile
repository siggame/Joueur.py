FROM siggame/joueur:py-onbuild as build

FROM siggame/joueur:py-base

COPY --from=build --chown=siggame:siggame /usr/src/client /client
