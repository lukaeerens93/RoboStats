classdef gameGaussian < Game
    %GAMEGAUSSIAN This is a concrete class defining a game where rewards a
    %   are drawn from a gaussian distribution.
    
    methods
        
        function self = gameGaussian(nbActions, totalRounds) 
            % Input
            %   nbActions - number of actions
            %   totalRounds - number of rounds of the game
            self.nbActions = nbActions;
            self.totalRounds = totalRounds;
            
            % To make this, this.. tHING less verbose when called later
            nbA = nbActions;     
            tR = totalRounds;
            
            % Resets the current counter to the beginning
            self.N = 0;  
            
            % Tabulate the reward signals
            self.tabR = normrnd(0, 1, [nbA,tR] ); % table of rewards
        end
        
    end    
end

