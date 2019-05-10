classdef gameAdversarial<Game
    %GAMEADVERSARIAL This is a concrete class defining a game where rewards
    %   are adversarially chosen.

    methods
        
        function self = gameAdversarial(nbActions, totalRounds)

            self.nbActions = nbActions;
            self.totalRounds = totalRounds;
            
            % To make it less verbose
            nbA = nbActions;
            tR = totalRounds;
            
            % Resets the current counter to the beginning
            self.N = 0; 
            
            % Define the array (table of rewards)
            self.tabR = [];
            
            % this incrememnts with each loop
            whatever = 0;
            
            for i = 1:totalRounds
                
                if ( whatever == 0 )
                    self.tabR =[self.tabR, [0.8;0.2] ];
                end
                
                if ( whatever == 1)
                    self.tabR =[self.tabR, [0.7;0.3] ];
                end
                
                if ( whatever == 2 )
                    self.tabR =[self.tabR, [0.6;0.4] ];
                end
                
                if ( whatever == 3)
                    self.tabR =[self.tabR, [0.5;0.5] ];
                end
                
                if ( whatever == 4 )
                    self.tabR =[self.tabR, [0.6;0.4] ];
                end
                
                if ( whatever == 5)
                    self.tabR =[self.tabR, [0.7;0.3] ];
                end
                
                if ( whatever == 6)
                    self.tabR =[self.tabR, [0.8;0.2] ];
                end
                

                whatever = whatever + 1
                % reset the whatever variable to 0
                if ( whatever == 7)
                    whatever = 0;
                end

            end
            
        end
   
    end    
end

