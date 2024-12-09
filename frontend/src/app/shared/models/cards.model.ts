export interface MinimumCards {
    tipo: TypeCardsEnum,
    nome: string,
    classificacao: string

}

export enum TypeCardsEnum {
    BARALHO = "BARALHO",
    CONVERSA = "CONVERSA",
    PAPEL = "PAPEL"
}

