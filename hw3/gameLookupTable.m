classdef gameLookupTable < Game
    %GAMELOOKUPTABLE This is a concrete class defining a game defined by an
    %external input
    
    methods
        function self = gameLookupTable(tabInput, isLoss)
            % Input
            %   tabInput - input table (actions x rewards or losses)
            %   isLoss - 1 if input table represent loss, 0 otherwise
            self.N = 0;
            if(tabInput ~= "game")
                input = struct2cell( load(tabInput) );
                if (isLoss == 0)    %if no loss
                    self.tabR = input{1};
                end
                if (isLoss == 1)    %if there is a loss
                    self.tabR = 1 - input{1};
                end
                [self.nbActions, self.totalRounds] = size( input{1} );
            end
        end
        
    end
    
end
