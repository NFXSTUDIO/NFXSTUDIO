import java.util.Scanner;

public class TicTacToe {

    int BOARDSIZE = 3;
    Status status;
    char[][] board;
    boolean firstPlayer;
    boolean gameOver;

    void play(){
        Scanner scanner = new Scanner(System.in);

        status = Status.CONTINUE;
        board = new char[3][3];
        //set values of array
        for(int x = 0; x < 3; x++){
            for(int y = 0; y < 3; y++){
                board[x][y] = ' ';
            }
        }
        firstPlayer = true;
        gameOver = false;
        //loop until game end
        while(true){ //break will happen after board is displayed
            //set current player char
            char pieceToPlay;
            if(firstPlayer)
                pieceToPlay = 'X';
            else
                pieceToPlay = 'O';

            //print board status
            printBoard();
            System.out.println();
            if(firstPlayer)
                printStatus(0);
            else
                printStatus(1);

            //if state is not continue, break
            if(status != Status.CONTINUE){
                break;
            }

            //player input
            int rowMove = 0;
            int columnMove = 0;
            //loop until valid input made
            do{
                System.out.print("Player " + pieceToPlay + ": Enter row (0, 1 or 2): ");
                String rowString = scanner.nextLine();
                System.out.print("Player " + pieceToPlay + ": Enter column (0, 1 or 2): ");
                String columnString = scanner.nextLine();
                //try to convert input string to int
                try{
                    rowMove = Integer.parseInt(rowString);
                    columnMove = Integer.parseInt(columnString);
                }catch(Exception ignored){}
            }while(!validMove(rowMove, columnMove));

            //move is valid, now update the board
            board[columnMove][rowMove] = pieceToPlay;

            //if there's 3 in a row, set state to win
            //2 win conditions:
            //1. one column or row contains 3
            //2. has board[1][1], and either board[0][0]+board[2][2] or board[0][2]+board[2][0]

            int[] symbolsInRow = new int[3];
            int[] symbolsInColumn = new int[3];
            //count all the symbols
            for(int row = 0; row < 3; row++){
                for(int column = 0; column < 3; column++){
                    if(board[column][row] == pieceToPlay){
                        symbolsInRow[row]++;
                        symbolsInColumn[column]++;
                    }
                }
            }
            //win condition 1
            for(int x = 0; x < 3; x++){
                if(symbolsInRow[x] == 3 || symbolsInColumn[x] == 3){
                    status = Status.WIN;
                    break;
                }
            }
            if(status == Status.WIN)
                continue;
            //win condition 2
            if(board[1][1] == pieceToPlay &&
                (
                    (board[0][0] == pieceToPlay && board[2][2] == pieceToPlay)
                    || (board[0][2] == pieceToPlay && board[2][0] == pieceToPlay)
                )
            ){
                status = Status.WIN;
                continue;
            }

            //draw condition: all spaces are full
            boolean isDraw = true;
            for(int x = 0; x < 3; x++){
                for(int y = 0; y < 3; y++){
                    if(board[x][y] == ' '){
                        isDraw = false;
                        break;
                    }
                }
            }
            if(isDraw){
                status = Status.DRAW;
                continue;
            }

            //game has not ended; proceed to next player's turn
            firstPlayer = !firstPlayer;

        }
    }

    //precondition: player is 0 or 1
    void printStatus(int player){
        if(status == Status.DRAW){
            System.out.println("Draw.");
            return;
        }
        if(player == 0)
            System.out.print("Player X");
        else
            System.out.print("Player O");
        if(status == Status.CONTINUE){
            System.out.println("'s turn.");
        }else{
            System.out.println(" wins.");
        }
    }

    //this method ended up unused since all code to run a game ended up inside the TicTacToe class.
    Status gameStatus(){
        return status;
    }

    void printBoard(){
        System.out.println(" _______________________ ");
        for(int y = 0; y < 3; y++){
            System.out.println("|       |       |       |");

            for(int x = 0; x < 3; x++){
                System.out.print("|   ");
                System.out.print(board[x][y]);
                System.out.print("   ");
            }
            System.out.println("|");

            System.out.println("|_______|_______|_______|");
        }
    }

    //this method from the template seemed unnecessary and also the input doesn't make sense, so I've left it out
    /*void printSymbol(int column, char value){

    }*/

    boolean validMove(int row, int column){
        if(row < 0 || column < 0 || row > 2 || column > 2)
            return false;
        return board[column][row] == ' ';
    }

}

enum Status{
    WIN, DRAW, CONTINUE
}