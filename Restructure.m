function restructure(pathofthefolder)
        %
%get all the folders in the path

folders=ls(pathofthefolder);

folders_restruct=[1:110];
mkdir('\\toaster\homes\h\a\hameedul040\nt\AccountSettings\Desktop\Restructure')
%create all the substructures in the folder
for i=1:length(folders_restruct)
    folder_name=strcat('\\toaster\homes\h\a\hameedul040\nt\AccountSettings\Desktop\Restructure','\','char_',string(folders_restruct(i)));
    mkdir(char(folder_name));
end

restruct_folder='\\toaster\homes\h\a\hameedul040\nt\AccountSettings\Desktop\Restructure';

for i=3:size(folders,1)
    folder_path=strcat(pathofthefolder,'\',strtrim(folders(i,:)));
    files_in_the_folder=ls(folder_path);
    count=2;
    for j=3:size(files_in_the_folder,1)
        file_name=strtrim(files_in_the_folder(j,:));
        if ~strcmp(file_name,'000t01.tiff') && ~strcmp(file_name,'000t02.tiff')
            char_no=floor(count/2);
            %I have to write this in the folder char_char_no
            new_file_name=strcat(restruct_folder,'\char_',char(string(char_no)),'\',folders(i,:),'_',file_name);
            copyfile(strcat(folder_path,'\',file_name),new_file_name);
            count=count+1;
        end
    end
end



end
