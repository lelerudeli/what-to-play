import { Jogo } from "./jogo.model";

export interface Profile {
    nomeUsuario: string,
    nomeCompleto: string,
    jogos: Jogo[],
    quantidadeJogos: number,
    emailUsuario: string,
}