Configuration: {'root_dir': '/Users/km1/2code/python-projects/gpt-subtrans/.', 'file_extensions': ['py', 'js', 'ts', 'go', 'html']}
# Code Structure Documentation

## File: gui-subtrans.py
### Functions
- parse_arguments()
- run_with_profiler(app)

## File: gpt-subtrans.py

## File: run_tests.py
### Functions
- run_all_tests(tests_directory, subtitles_directory, results_directory)

## File: PySubtitleGPT/SubtitleBatch.py
### Class: SubtitleBatch
- __init__(self, dct)
- __str__(self)
- __repr__(self)
- originals(self)
- size(self)
- translated(self)
- untranslated(self)
- all_translated(self)
- start(self)
- srt_start(self)
- end(self)
- srt_end(self)
- duration(self)
- first_line_number(self)
- last_line_number(self)
- originals(self, value)
- translated(self, value)
- AddLine(self, line)
- AddTranslatedLine(self, line)
- HasTranslatedLine(self, line_number)
- AddContext(self, key, value)
- GetContext(self, key)
- SetContext(self, context)
- UpdateContext(self, update)
- Validate(self, options)
- PerformInputSubstitutions(self, substitutions, match_partial_words)
- PerformOutputSubstitutions(self, substitutions, match_partial_words)
- ConvertWhitespaceBlocksToNewlines(self)
- MergeLines(self, original_lines, translated_lines)

## File: PySubtitleGPT/SubtitleLine.py
### Class: SubtitleLine
- __init__(self, line, translation, original)
- __str__(self)
- __repr__(self)
- key(self)
- number(self)
- text(self)
- text_normalized(self)
- start(self)
- srt_start(self)
- end(self)
- srt_end(self)
- duration(self)
- line(self)
- translated(self)
- item(self)
- Construct(cls, number, start, end, text, original)
- FromDictionary(cls, values)
- FromMatch(cls, match)
- item(self, item)
- number(self, value)
- text(self, text)
- start(self, time)
- end(self, time)
- GetLines(lines)
- GetLineItems(cls, lines, tag)
- GetLineItem(cls, line, tag)
- MergeSubtitles(cls, merged_lines)

## File: PySubtitleGPT/Options.py
### Class: Options
- __init__(self, options)
- get(self, option, default)
- add(self, option, value)
- update(self, options)
- api_key(self)
- api_base(self)
- allow_multithreaded_translation(self)
- ReplaceTagsWithOptions(self, text)
- GetNonProjectSpecificOptions(self)
- GetSettings(self)
- Load(self)
- Save(self)
- InitialiseInstructions(self)
- _update_settings_version(self, settings)
### Functions
- env_bool(key, default)
- LoadInstructionsFile(filepath)

## File: PySubtitleGPT/TranslationEvents.py
### Class: TranslationEvents

## File: PySubtitleGPT/VersionCheck.py
### Functions
- CheckIfUpdateAvailable()
- CheckIfUpdateCheckIsRequired()

## File: PySubtitleGPT/SubtitleSerialisation.py
### Class: SubtitleEncoder
- default(self, obj)
- serialize_object(self, obj)
### Class: SubtitleDecoder
- __init__(self)
- object_hook(self, dct)
### Functions
- classname(obj)

## File: PySubtitleGPT/version.py

## File: PySubtitleGPT/SubtitleScene.py
### Class: SubtitleScene
- __init__(self, dct)
- __str__(self)
- __repr__(self)
- batches(self)
- size(self)
- linecount(self)
- first_line_number(self)
- last_line_number(self)
- all_translated(self)
- any_translated(self)
- summary(self)
- summary(self, value)
- batches(self, value)
- GetBatch(self, batch_number)
- AddBatch(self, batch)
- AddNewBatch(self)
- AddContext(self, key, value)
- GetContext(self, key)
- UpdateContext(self, update)
- MergeScenes(self, merged_scenes)
- MergeBatches(self, batch_numbers)
- SplitBatch(self, batch_number, line_number, translated_number)
- _renumber_batches(self)

## File: PySubtitleGPT/log_config.py
### Functions
- setup_logging()

## File: PySubtitleGPT/ChatGPTTranslation.py
### Class: ChatGPTTranslation
- __init__(self, response, prompt)
- ParseResponse(self)
- text(self)
- has_translation(self)
- user_prompt(self)
- summary(self)
- scene(self)
- synopsis(self)
- characters(self)
- full_text(self)
- reached_token_limit(self)
- quota_reached(self)
- PerformSubstitutions(self, substitutions, match_partial_words)

## File: PySubtitleGPT/ChatGPTTranslationParser.py
### Class: ChatGPTTranslationParser
- __init__(self, options)
- ProcessChatGPTResponse(self, translation)
- FindMatches(self, text, template)
- MatchTranslations(self, originals)
- TryFuzzyMatches(self, unmatched)
- ValidateTranslations(self)

## File: PySubtitleGPT/ChatGPTPrompt.py
### Class: ChatGPTPrompt
- __init__(self, instructions)
- GenerateMessages(self, prompt, lines, context)
- GenerateRetryPrompt(self, reponse, retry_instructions, errors)
- GenerateBatchPrompt(self, prompt, lines, tag_lines)
- GetLinePrompt(self, line)

## File: PySubtitleGPT/SubtitleValidator.py
### Class: SubtitleValidator
- __init__(self, options)
- ValidateTranslations(self, translated)

## File: PySubtitleGPT/SubtitleError.py
### Class: SubtitleError
- __init__(self, message, error)
- __str__(self)
### Class: TranslationError
- __init__(self, message, error)
### Class: TranslationImpossibleError
- __init__(self, message, translation, error)
### Class: TranslationAbortedError
- __init__(self, translation)
### Class: TranslationFailedError
- __init__(self, message, translation, error)
### Class: NoTranslationError
- __init__(self, message, response)
### Class: UntranslatedLinesError
- __init__(self, message, lines)
- __str__(self)
### Class: UnmatchedLinesError
- __init__(self, message, lines)
### Class: EmptyLinesError
- __init__(self, message, lines)
### Class: TooManyNewlinesError
- __init__(self, message, lines)
### Class: LineTooLongError
- __init__(self, message, lines)

## File: PySubtitleGPT/SubtitleTranslator.py
### Class: SubtitleTranslator
- __init__(self, subtitles, options)
- GetAvailableModels(cls, api_key, api_base)
- StopTranslating(self)
- TranslateSubtitles(self)
- TranslateScene(self, scene, batch_numbers, remaining_lines)
- TranslateBatches(self, batches, context, remaining_lines)
- ProcessTranslation(self, batch, context, client)
- RequestRetranslations(self, client, batch, translation)
- SanitiseSummary(self, summary)

## File: PySubtitleGPT/SubtitleProject.py
### Class: SubtitleProject
- __init__(self, options)
- __del__(self)
- Initialise(self, filepath, outputpath)
- TranslateSubtitles(self)
- SaveSubtitles(self, outputpath)
- TranslateScene(self, scene_number, batch_numbers, translator)
- AnyTranslated(self)
- GetProjectFilepath(self, filepath)
- GetBackupFilepath(self, filepath)
- LoadSubtitleFile(self, filepath)
- WriteProjectFile(self, projectfile)
- WriteBackupFile(self)
- ReadProjectFile(self)
- UpdateProjectFile(self)
- UpdateProjectOptions(self, options)
- _start_autosave_thread(self)
- _background_autosave(self)
- _on_preprocessed(self, scenes)
- _on_batch_translated(self, batch)
- _on_scene_translated(self, scene)

## File: PySubtitleGPT/SubtitleBatcher.py
### Class: BaseSubtitleBatcher
- __init__(self, options)
- BatchSubtitles(self, lines)
### Class: OldSubtitleBatcher
- __init__(self, options)
- BatchSubtitles(self, lines)
### Class: SubtitleBatcher
- __init__(self, options)
- BatchSubtitles(self, lines)
- _create_scene(self, current_lines)
- _split_lines(self, lines)
### Functions
- CreateSubtitleBatcher(options)

## File: PySubtitleGPT/SubtitleFile.py
### Class: SubtitleFile
- __init__(self, filepath, outputpath)
- has_subtitles(self)
- linecount(self)
- scenecount(self)
- scenes(self)
- scenes(self, scenes)
- GetScene(self, scene_number)
- GetBatch(self, scene_number, batch_number)
- GetBatchContainingLine(self, line_number)
- GetBatchContext(self, scene_number, batch_number, max_lines)
- LoadSubtitles(self, filepath)
- SaveOriginals(self, path)
- SaveTranslation(self, outputpath, include_original)
- UpdateContext(self, options)
- AutoBatch(self, options)
- AddScene(self, scene)
- UpdateScene(self, scene_number, update)
- UpdateBatch(self, scene_number, batch_number, update)
- UpdateLineText(self, line_number, original_text, translated_text)
- MergeScenes(self, scene_numbers)
- MergeBatches(self, scene_number, batch_numbers)
- MergeLines(self, hierarchy)
- SplitScene(self, scene_number, batch_number)
- Renumber(self)
- Sanitise(self)
- _merge_original_and_translated(self, originals, translated)

## File: PySubtitleGPT/Helpers.py
### Functions
- Linearise(lines)
- UpdateFields(item, update, fields)
- CreateSrtSubtitle(item)
- GetTimeDelta(time)
- GetInputPath(filepath)
- GetOutputPath(filepath)
- GenerateTagLines(context, tags)
- GenerateTag(tag, content)
- BuildPrompt(options)
- ParseTranslation(text)
- ExtractTag(tagname, text)
- ExtractTagList(tagname, text)
- MergeTranslations(lines, translated)
- UnbatchScenes(scenes)
- ResyncTranslatedLines(original_lines, translated_lines)
- ParseCharacters(character_list)
- ParseSubstitutions(sub_list, separator)
- PerformSubstitutions(substitutions, input, match_partial_words)
- RemoveWhitespaceAndPunctuation(string)
- IsTextContentEqual(string1, string2)
- ParseDelayFromHeader(value)
- FormatMessages(messages)

## File: PySubtitleGPT/ChatGPTClient.py
### Class: ChatGPTClient
- __init__(self, options, instructions)
- RequestTranslation(self, prompt, lines, context)
- RequestRetranslation(self, translation, errors)
- SendMessages(self, messages, temperature)

## File: Tests/SubtitleBatcherTests.py
### Functions
- configure_logger(filename, logger_name)
- analyze_scenes(scenes)
- run_test(subtitles, logger, options)
- run_tests(directory_path, results_path)

## File: GUI/ProjectViewModelUpdate.py
### Class: ModelUpdateSection
- __init__(self)
- update(self, key, item_update)
- replace(self, key, item)
- add(self, key, item)
- remove(self, key)
- HasUpdate(self)
### Class: ModelUpdate
- __init__(self)
- HasUpdate(self)

## File: GUI/SettingsDialog.py
### Class: SettingsDialog
- __init__(self, options, parent)
- create_section_widget(self, settings, section_name)
- accept(self)
- reject(self)

## File: GUI/Command.py
### Class: Command
- __init__(self, datamodel)
- SetDataModel(self, datamodel)
- SetCallback(self, callback)
- SetUndoCallback(self, undo_callback)
- Abort(self)
- run(self)
- execute(self)
- undo(self)
- on_abort(self)
- execute_callback(self)
- execute_undo_callback(self)
### Class: CommandError
- __init__(self, command)

## File: GUI/TranslatorOptions.py
### Class: TranslatorOptionsDialog
- __init__(self, data, parent)
- _add_form_option(self, key, initial_value, key_type, tooltip)
- _create_button(self, text, on_click)
- accept(self)
- reject(self)
- _check_for_edited_instructions(self)
- load_icon(self)
- save_icon(self)
- _load_instructions(self)
- _save_instructions(self)
- set_defaults(self)

## File: GUI/ProjectToolbar.py
### Class: ProjectToolbar
- __init__(self, parent)
- _toggle_options(self)
- show_options(self)
- show_options(self, value)
- show_options_icon(self)

## File: GUI/FirstRunOptions.py
### Class: FirstRunOptions
- __init__(self, data, parent)
- accept(self)
- _on_free_plan_changed(self)

## File: GUI/SubtitleItemDelegate.py
### Class: SubtitleItemDelegate
- __init__(self, parent)
- createEditor(self, parent, option, index)
- paint(self, painter, option, index)

## File: GUI/ProjectDataModel.py
### Class: ProjectDataModel
- __init__(self, project, options)
- UpdateOptions(self, options)
- IsProjectInitialised(self)
- NeedsSave(self)
- NeedsAutosave(self)
- SaveProject(self)
- GetLock(self)
- RegisterActionHandler(cls, action_name, handler)
- PerformModelAction(self, action_name, params)
- CreateViewModel(self)
- UpdateViewModel(self, update)

## File: GUI/MainToolbar.py
### Class: MainToolbar
- __init__(self, handler)
- EnableActions(self, action_list)
- DisableActions(self, action_list)
- SetBusyStatus(self, datamodel, command_queue)

## File: GUI/ScenesBatchesModel.py
### Class: ScenesBatchesModel
- __init__(self, viewmodel, parent)
- filterAcceptsRow(self, source_row, source_parent)
- data(self, index, role)

## File: GUI/MainWindow.py
### Class: MainWindow
- __init__(self, parent, options, filepath)
- QueueCommand(self, command)
- ShowSettingsDialog(self)
- ShowAboutDialog(self)
- PrepareForSave(self)
- closeEvent(self, e)
- _load_icon(self, name)
- _on_action_requested(self, action_name, params)
- _on_command_added(self, command)
- _on_command_complete(self, command, success)
- _update_status_bar(self, command, succeeded)
- _update_main_toolbar(self)
- _on_project_options_changed(self, options)
- _first_run(self, options)
- _show_new_project_Settings(self, project)
- _on_error(self, error)
### Functions
- LoadStylesheet(name)

## File: GUI/AboutDialog.py
### Class: AboutDialog
- __init__(self, parent)

## File: GUI/ProjectViewModel.py
### Class: ViewModelItem
- GetContent(self)
### Class: ViewModelError
- __init__(self, message, error)
### Class: ProjectViewModel
- __init__(self)
- getRootItem(self)
- AddUpdate(self, update)
- ProcessUpdates(self)
- CreateModel(self, data)
- CreateSceneItem(self, scene)
- CreateBatchItem(self, scene_number, batch)
- GetLineItem(self, line_number, get_translated)
- GetBatchNumbers(self)
- Remap(self)
- ApplyUpdate(self, update)
- AddScene(self, scene)
- ReplaceScene(self, scene)
- UpdateScene(self, scene_number, scene_update)
- RemoveScene(self, scene_number)
- AddBatch(self, batch)
- ReplaceBatch(self, batch)
- UpdateBatch(self, scene_number, batch_number, batch_update)
- RemoveBatch(self, scene_number, batch_number)
- AddOriginalLine(self, scene_number, batch_number, line)
- UpdateOriginalLine(self, scene_number, batch_number, line_number, line_update)
- UpdateOriginalLines(self, scene_number, batch_number, lines)
- RemoveOriginalLine(self, scene_number, batch_number, line_number)
- AddTranslatedLine(self, scene_number, batch_number, line)
- UpdateTranslatedLine(self, scene_number, batch_number, line_number, line_update)
- UpdateTranslatedLines(self, scene_number, batch_number, lines)
- RemoveTranslatedLine(self, scene_number, batch_number, line_number)
### Class: LineItem
- __init__(self, is_translation, line_number, model)
- Update(self, line_update)
- __str__(self)
- __repr__(self)
- start(self)
- end(self)
- text(self)
- scene(self)
- batch(self)
### Class: BatchItem
- __init__(self, scene_number, batch)
- AddLineItem(self, is_translation, line_number, model)
- original_count(self)
- translated_count(self)
- all_translated(self)
- start(self)
- end(self)
- context(self)
- summary(self)
- response(self)
- first_line_number(self)
- last_line_number(self)
- has_errors(self)
- Update(self, update)
- GetContent(self)
- _update_first_and_last(self)
- _invalidate_first_and_last(self)
- _get_errors(self, errors)
- __str__(self)
### Class: SceneItem
- __init__(self, scene)
- AddBatchItem(self, batch_item)
- batch_count(self)
- translated_batch_count(self)
- original_count(self)
- translated_count(self)
- all_translated(self)
- has_errors(self)
- start(self)
- end(self)
- duration(self)
- summary(self)
- Update(self, update)
- GetContent(self)
- __str__(self)

## File: GUI/SubtitleListModel.py
### Class: SubtitleListModel
- __init__(self, show_translated, viewmodel, parent)
- ShowSelection(self, selection)
- ShowSelectedBatches(self, batch_numbers)
- mapFromSource(self, source_index)
- mapToSource(self, index)
- rowCount(self, parent)
- columnCount(self, parent)
- parent(self, index)
- index(self, row, column, parent)
- data(self, index, role)
- _update_visible_batches(self)
- _reset_visible_batches(self)

## File: GUI/ScenesBatchesDelegate.py
### Class: ScenesBatchesDelegate
- __init__(self, parent)
- paint(self, painter, option, index)

## File: GUI/ProjectCommands.py
### Class: BatchSubtitlesCommand
- __init__(self, project)
- execute(self)
- undo(self)
### Class: MergeScenesCommand
- __init__(self, scene_numbers, datamodel)
- execute(self)
### Class: MergeBatchesCommand
- __init__(self, scene_number, batch_numbers, datamodel)
- execute(self)
- undo(self)
### Class: MergeLinesCommand
- __init__(self, selection, datamodel)
- execute(self)
- undo(self)
### Class: SplitBatchCommand
- __init__(self, scene_number, batch_number, line_number, translation_number, datamodel)
- execute(self)
- undo(self)
### Class: SplitSceneCommand
- __init__(self, scene_number, batch_number, datamodel)
- execute(self)
- undo(self)
### Class: TranslateSceneCommand
- __init__(self, scene_number, batch_numbers, datamodel)
- execute(self)
- on_abort(self)
- _on_batch_translated(self, batch)
### Class: TranslateSceneMultithreadedCommand
- __init__(self, scene_number, batch_numbers, datamodel)
### Class: ResumeTranslationCommand
- __init__(self, datamodel, multithreaded)
- execute(self)
### Class: SwapTextAndTranslations
- __init__(self, scene_number, batch_number, datamodel)
- execute(self)

## File: GUI/ProjectActions.py
### Class: ActionError
- __init__(self, message, error)
- __str__(self)
### Class: NoApiKeyError
- __init__(self)
### Class: ProjectActions
- __init__(self, mainwindow, datamodel)
- SetDataModel(self, datamodel)
- AddAction(self, name, function, icon, shortcut, tooltip)
- GetAction(self, name)
- GetActionList(self, names)
- _issue_command(self, command)
- _check_api_key(self)
- _quit(self)
- _load_subtitle_file(self)
- _save_project_file(self)
- _is_shift_pressed(self)
- _toggle_project_options(self)
- _show_settings_dialog(self)
- _show_about_dialog(self)
- _validate_datamodel(self, datamodel)
- _start_translating(self)
- _start_translating_fast(self)
- _stop_translating(self)
- _translate_selection(self, datamodel, selection)
- _update_scene(self, datamodel, scene_number, update)
- _update_batch(self, datamodel, scene_number, batch_number, update)
- _update_line(self, datamodel, line_number, original_text, translated_text)
- _merge_selection(self, datamodel, selection)
- _split_batch(self, datamodel, selection)
- _split_scene(self, datamodel, selection)
- _swap_text_and_translation(self, datamodel, selection)

## File: GUI/ProjectSelection.py
### Class: SelectionScene
- __init__(self, scene, selected)
- __getitem__(self, index)
- __setitem__(self, index, value)
- __str__(self)
- __repr__(self)
### Class: SelectionBatch
- __init__(self, batch, selected)
- __str__(self)
- __repr__(self)
### Class: SelectionLine
- __init__(self, scene, batch, number, selected)
- __str__(self)
- __repr__(self)
### Class: ProjectSelection
- __init__(self)
- scene_numbers(self)
- selected_scenes(self)
- batch_numbers(self)
- selected_batches(self)
- original_lines(self)
- selected_originals(self)
- translated_lines(self)
- selected_translated(self)
- Any(self)
- AnyScenes(self)
- OnlyScenes(self)
- AnyBatches(self)
- OnlyBatches(self)
- AnyLines(self)
- AllLinesInSameBatch(self)
- MatchingLines(self)
- MultipleSelected(self, max)
- IsContiguous(self)
- IsFirstInBatchSelected(self)
- IsFirstOrLastInBatchSelected(self)
- IsFirstInSceneSelected(self)
- IsFirstOrLastInSceneSelected(self)
- GetHierarchy(self)
- AppendItem(self, model, index, selected)
- AddSelectedLines(self, selected_originals, selected_translations)
- __str__(self)
- __repr__(self)
- str_scenes(self)
- str_batches(self)
- str_originals(self)
- str_selected_originals(self)
- str_translated(self)
- str_selected_translated(self)
- str_lines(self)
- _count(self, num, singular, plural)

## File: GUI/CommandQueue.py
### Class: ClearCommandQueue
- __init__(self, datamodel)
- execute(self)
### Class: CommandQueue
- __init__(self, parent)
- SetMaxThreadCount(self, count)
- queue_size(self)
- Stop(self)
- AddCommand(self, command, datamodel, callback, undo_callback)
- Contains(self, command_type, type_list)
- AnyCommands(self)
- AnyBlocking(self)
- _on_command_executed(self, command, success)
- _queue_command(self, command, datamodel, callback, undo_callback)
- _start_command_queue(self)
- _clear_command_queue(self)

## File: GUI/GuiHelpers.py
### Functions
- GetResourcePath(relative_path)
- GetThemeNames()
- GetInstructionFiles()
- GetLineHeight(text, wrap_length)

## File: GUI/NewProjectSettings.py
### Class: NewProjectSettings
- __init__(self, project, parent)
- accept(self)
- _update_settings(self)
- _preview_batches(self)
- _update_inputs(self)

## File: GUI/FileCommands.py
### Class: LoadSubtitleFile
- __init__(self, filepath, options)
- execute(self)
- undo(self)
### Class: SaveProjectFile
- __init__(self, project, filepath)
- execute(self)
### Class: SaveSubtitleFile
- __init__(self, filepath, project)
- execute(self)
### Class: SaveTranslationFile
- __init__(self, filepath, project)
- execute(self)

## File: GUI/Widgets/MenuBar.py
### Class: ProjectMenuBar
- __init__(self, parent)

## File: GUI/Widgets/OptionsWidgets.py
### Class: OptionWidget
- __init__(self, key, initial_value, parent, tooltip)
- GenerateName(key)
- GetValue(self)
- SetValue(self, value)
### Class: TextOptionWidget
- __init__(self, key, initial_value, tooltip)
- GetValue(self)
- SetValue(self, value)
### Class: MultilineTextOptionWidget
- __init__(self, key, initial_value, tooltip)
- GetValue(self)
- SetValue(self, value)
- SetReadOnly(self, is_read_only)
- _get_content(self, value)
- _encode_content(self, obj)
### Class: IntegerOptionWidget
- __init__(self, key, initial_value, tooltip)
- GetValue(self)
- SetValue(self, value)
- SetRange(self, min, max)
- SetEnabled(self, enabled)
### Class: FloatOptionWidget
- __init__(self, key, initial_value, tooltip)
- GetValue(self)
- SetValue(self, value)
- SetRange(self, min, max)
- SetEnabled(self, enabled)
### Class: CheckboxOptionWidget
- __init__(self, key, initial_value, tooltip)
- GetValue(self)
- SetValue(self, checked)
- SetEnabled(self, enabled)
### Class: DropdownOptionWidget
- __init__(self, key, values, initial_value, tooltip)
- GetValue(self)
- SetValue(self, value)
### Functions
- CreateOptionWidget(key, initial_value, key_type, tooltip)

## File: GUI/Widgets/Editors.py
### Class: EditDialog
- __init__(self, model, parent, title)
- GetFormLayout(self)
- SetTabLayout(self, tab_widget, layout, title)
- AddMultilineEdit(self, form_layout, key, read_only)
- UpdateModelFromEditor(self, key)
- CreateEditor(self)
- UpdateModel(self)
- accept(self)
### Class: EditSceneDialog
- __init__(self, item, parent)
- CreateEditor(self)
- UpdateModel(self)
### Class: EditBatchDialog
- __init__(self, item, parent)
- CreateEditor(self)
- UpdateModel(self)
### Class: EditSubtitleDialog
- __init__(self, original, translated, parent)
- CreateEditor(self)
- UpdateModel(self)

## File: GUI/Widgets/ModelView.py
### Class: ModelView
- __init__(self, parent)
- SetDataModel(self, datamodel)
- SetViewModel(self, viewmodel)
- SetProjectOptions(self, options)
- ToggleProjectOptions(self, show)
- CloseProjectOptions(self)
- GetSelection(self)
- _items_selected(self)
- _lines_selected(self)
- _on_scene_edited(self, scene_number, scene_model)
- _on_batch_edited(self, scene, batch_number, batch_model)

## File: GUI/Widgets/Widgets.py
### Class: TreeViewItemWidget
- __init__(self, content, parent)
- _set_properties(self, widget, properties)
### Class: WidgetHeader
- __init__(self, text, parent)
### Class: WidgetSubheading
- __init__(self, text, parent)
### Class: WidgetBody
- __init__(self, text, parent)
### Class: LineItemView
- __init__(self, line, parent)
### Class: LineItemHeader
- __init__(self, line, parent)
### Class: LineItemBody
- __init__(self, line, parent)
### Class: OptionsGrid
- __init__(self, parent)
### Class: TextBoxEditor
- focusInEvent(self, e)
- focusOutEvent(self, e)
- SetText(self, text)

## File: GUI/Widgets/LogWindow.py
### Class: LogWindow
- __init__(self, parent)
- SetLoggingLevel(self, level)
- AppendLogMessage(self, message, level)
- _scroll_to_bottom(self)
### Class: QtLogHandler
- __init__(self, log_window)
- emit(self, record)

## File: GUI/Widgets/ContentView.py
### Class: ContentView
- __init__(self, parent)
- ShowSelection(self, selection)
- Populate(self, viewmodel)
- Clear(self)
- GetSelectedLines(self)
- ClearSelectedLines(self)
- _originals_selected(self, originals)
- _translations_selected(self, translations)
- _edit_line(self, item)
- _update_view_model(self)

## File: GUI/Widgets/ProjectOptions.py
### Class: ProjectOptions
- __init__(self, options)
- GetOptions(self)
- AddSingleLineOption(self, row, label, options, key)
- AddMultiLineOption(self, row, label, options, key)
- AddCheckboxOption(self, row, label, options, key)
- AddButtonOption(self, row, label, text, callable)
- Populate(self, options)
- Clear(self)
- _setvalue(self, key, value)
- _settext(self, key, value)
- _text_changed(self, text)
- _check_changed(self, int)
- _gpt_settings(self)

## File: GUI/Widgets/ScenesView.py
### Class: ScenesView
- __init__(self, parent, viewmodel)
- Clear(self)
- Populate(self, viewmodel)
- SelectAll(self)
- _item_selected(self, selected, deselected)
- _select_children(self, model, index, data)
- _deselect_children(self, model, index, item)
- _deselect_parent(self, model, index)
- keyPressEvent(self, event)
- _on_double_click(self, index)
- _edit_scene(self, item)
- _edit_batch(self, item)

## File: GUI/Widgets/SubtitleView.py
### Class: SubtitleView
- __init__(self, show_translated, parent)
- SetViewModel(self, viewmodel)
- ShowSelection(self, selection)
- GetSelectedLines(self)
- ClearSelectedLines(self)
- SelectSubtitles(self, line_numbers)
- SelectAll(self)
- SynchroniseScrollbar(self, scrollbar)
- _partner_scrolled(self, value)
- _on_double_click(self, index)
- selectionChanged(self, selected, deselected)
- keyPressEvent(self, event)

## File: GUI/Widgets/SelectionView.py
### Class: SelectionView
- __init__(self)
- ShowSelection(self, selection)
- _create_button(self, text, on_click)
- _debug_text(self, selection)
- _on_translate_selection(self)
- _on_merge_selection(self)
- _on_split_batch(self)
- _on_split_scene(self)
- _on_swap_text(self)
### Functions
- _show(widget, condition)


