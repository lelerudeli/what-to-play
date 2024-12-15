export interface MinimumCards {
    tipo: TypeCardsEnum,
    nome: string,
    classificacao: ClassificacaoCards
}

export enum TypeCardsEnum {
    BARALHO = "1",
    CONVERSA = "2",
    PAPEL = "3"
}

export enum ClassificacaoCards {
    DEZOITO = "DEZOITO",
    DEZESSEIS = "DEZESSEIS",
    CATORZE = "CATORZE",
    DOZE = "DOZE",
    DEZ = "DEZ",
    LIVRE = "LIVRE"
}

