import shutil
from datetime import datetime

import click


# @click.command()
# @click.option('--file', help='process file other than /etc/hosts', required=False)
# def hosts_manager(enable, disable, file):
#
#     print(enable)
#     print(disable)


@click.command()
@click.option('--file', help="if not /etc/hosts", default='/etc/hosts', type=click.File(mode='r'))
@click.option('--dry-run', help="only pretend to", default=False, is_flag=True)
@click.option('-v', '--verbose', help="output resulting file at the end", default=False, is_flag=True)
@click.option('--backup/--no-backup', help="default: true", default=True, is_flag=True)
@click.argument('command', required=True)
@click.argument('sections', required=True, nargs=-1)
def hosts_manager(command, sections, *args, **kwargs):
    """
    enable|disable named sections in your hosts file
    filename.bak-YYYY-MM-DD is always created
    """
    if not command in ['enable', 'disable']:
        click.echo("command must be enable|disable")
        return

    file = kwargs.get('file')
    dry =  kwargs.get('dry_run')
    verbose =  kwargs.get('verbose')
    do_backup =  kwargs.get('backup')
    click.echo('processing section %s in %s' % ('|'.join(sections), file.name, ))
    lines = tuple(file)
    new_lines = []
    started = False
    for line in lines:
        modified = False
        if line.startswith('# end'):
            started = False
        if started:
            if command == 'enable':
                if line.startswith('#'):
                    new_lines.append(line[1:])
                    modified = True
            if command == 'disable':
                if not line.startswith('#'):
                    new_lines.append('#%s' % line)
                    modified = True
        for section in sections:
            if line.startswith('# start:%s' % section):
                started = True
        if not modified:
            new_lines.append(line)
    if dry or verbose:
        for l in new_lines:
            click.echo(l.strip())
    if not dry:
        if do_backup:
            backup = '%s.backup-%s' % (file.name, datetime.now().strftime("%Y-%m-%d--%H-%M-%S"))
            shutil.copy(file.name, backup)
            click.echo('backup file created: %s' % backup)
        write_file = open(file.name, 'w')
        write_file.writelines(new_lines)
        write_file.close()



if __name__ == '__main__':
    hosts_manager()